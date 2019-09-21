import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_os_type(host):
    assert host.system_info.type == 'linux', 'Only the Linux operating system is supported!'


def test_package(host):
    # Get the scheduler daemon name
    service_name = 'docker'
    package_name = 'docker-ce'

    # Check if the system has cron daemon installed, enabled, up and running
    assert host.package(package_name).is_installed, 'The %s package should be installed.' % package_name
    assert host.service(service_name).is_running, 'The %s daemon should be running.' % service_name
    assert host.service(service_name).is_enabled, 'The %s service should be enabled.' % service_name

    # Check if a system unit file exists
    system_unit = host.file('/etc/systemd/system/%s.service' % service_name)
    assert system_unit.exists, 'The system unit file should exists.'

    # Check if a system configuration file exists
    system_configuration = host.file('/etc/sysconfig/%s' % service_name)
    assert system_configuration.exists, 'The system configuration file should exists.'
    assert system_configuration.contains('--dns 1.1.1.1'), 'The system configuration file is incorrect.'

    # Check docker files directory
    assert host.file('/var/lib/%s' % service_name).exists, 'The docker files directory should exists.'


def test_configuration(host):
    # Configuration file must be in place
    configuration = host.file('/etc/docker/docker.json')
    assert configuration.exists, 'The configuration file should exists.'
    assert configuration.user == 'root'
    assert configuration.group == 'root'
    assert configuration.mode == 0o644

    # Check the UNIX socket group
    group = host.group('docker')
    assert group.exists, 'The daemon UNIX socket group should exists.'
