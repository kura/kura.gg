# nginx Embedded Perl module for adding a Content-MD5 HTTP header
#
# This perl module, will output an MD5 of a requested file using the
# Content-MD5 HTTP header, by either pulling it from a file of the
# same name with .md5 appended to the end, if it exists, or will
# calculate the MD5 hex hash on the fly
#
# Author: Matt Martz <matt@sivel.net>
# Link: https://gist.github.com/1870822#file_content_md5.pm
# License: http://www.nginx.org/LICENSE

package ContentMD5;
use nginx;
use Digest::MD5;

sub handler {
	my $r = shift;
	my $filename = $r->filename;

	return DECLINED unless -f $filename;

	my $content_length = -s $filename;
	my $md5;

	if ( -f "$filename.md5" ) {
		open( MD5FILE, "$filename.md5" ) or return DECLINED;
		$md5 = <MD5FILE>;
		close( MD5FILE );
		$md5 =~ s/^\s+//;
		$md5 =~ s/\s+$//;
		$md5 =~ s/\ .*//;
	} else {
		open( FILE, $filename ) or return DECLINED;
		my $ctx = Digest::MD5->new;
		$ctx->addfile( *FILE );
		$md5 = $ctx->hexdigest;
		close( FILE );
	}

	$r->header_out( "Content-MD5", $md5 ) unless ! $md5;

	return DECLINED;
}

1;
__END__