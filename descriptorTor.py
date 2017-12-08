from stem.descriptor.remote import DescriptorDownloader
downloader =DescriptorDownloader()
for descriptor in downloader.get_consensus().run():
	if descriptor.exit_policy.is_exiting_allowed():
		print descriptor

