Shared VMDKs on ESX vSphere
###########################
:date: 2011-07-09 02:07
:author: kura
:category: tutorials
:tags: esx, iscsi, scsi, shared vmdk, vmdk, vmware
:slug: shared-vmdks-on-esx-vsphere

I'd first like to point out that although the VMDKs are shared between
hosts using a shared SCSI BUS they are not synched, meaning that if you
write to the mounted point on any machine it will not display on other
machines with the same mount point until you remount the drive.
Annoying, but understandable.

To business.

First off all machines that you want to share this VMDK with will need
to be OFFLINE.

Next up we create the VMDK, I find it easiest to do this by adding
hardware to an already existing machine, I'm going to use one that I
want the VMDK shared with to make it even simpler.

.. image:: https://kura.io/images/shared-vmdks-on-esx-vsphere1.png

You will need to enable clustering features as shown below, this means
you cannot use thin provisioning.

.. image:: https://kura.io/images/shared-vmdks-on-esx-vsphere2.png

You will need to add the VMDK to a new SCSI BUS, this will usually begin
with 1: or 2: depending on how many SCSI BUS you have connected already,
I'm using 1:0 as shown below.

You will also need to set it's MODE as "Independent" and "Persistent".

.. image:: https://kura.io/images/shared-vmdks-on-esx-vsphere3.png

Once the drive has been added it will appear in your VM hardware list
along with the new SCSI controller. Click on the controller to modify it
and set it as "Physical" as shown below.

.. image:: https://kura.io/images/shared-vmdks-on-esx-vsphere4.png

Once this is down, close out of the hardware panel and modify the other
VMs you wish this disk to be shared to, do exactly as above but adding
the existing VMDK to each VM rather than creating a new drive.

When you're finished, power on all of the machines and mount the device
as you normally would for your operating system.
