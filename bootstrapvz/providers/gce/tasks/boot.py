from bootstrapvz.base import Task
from bootstrapvz.common import phases
from bootstrapvz.common.tasks import grub
import os.path


class ConfigureGrub(Task):
	description = 'Change grub configuration to allow for ttyS0 output'
	phase = phases.system_modification
	successors = [grub.InstallGrub_1_99, grub.InstallGrub_2]

	@classmethod
	def run(cls, info):
		from bootstrapvz.common.tools import sed_i
		grub_config = os.path.join(info.root, 'etc/default/grub')
		sed_i(grub_config, r'^(GRUB_CMDLINE_LINUX*=".*)"\s*$', r'\1console=ttyS0,38400n8 elevator=noop"')
		sed_i(grub_config, r'^.*(GRUB_TIMEOUT=).*$', r'GRUB_TIMEOUT=0')
		sed_i(grub_config, '^GRUB_HIDDEN_TIMEOUT=true', '#GRUB_HIDDEN_TIMEOUT=true')
