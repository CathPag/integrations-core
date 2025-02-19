# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>

from datadog_checks.base.utils.models.fields import get_default_field_value


def shared_service(field, value):
    return get_default_field_value(field, value)


def instance_blacklist_conntrack_metrics(field, value):
    return []


def instance_collect_aws_ena_metrics(field, value):
    return False


def instance_collect_connection_queues(field, value):
    return False


def instance_collect_connection_state(field, value):
    return False


def instance_collect_count_metrics(field, value):
    return False


def instance_collect_ethtool_metrics(field, value):
    return False


def instance_collect_rate_metrics(field, value):
    return True


def instance_combine_connection_states(field, value):
    return True


def instance_conntrack_path(field, value):
    return get_default_field_value(field, value)


def instance_disable_generic_tags(field, value):
    return False


def instance_empty_default_hostname(field, value):
    return False


def instance_excluded_interface_re(field, value):
    return get_default_field_value(field, value)


def instance_excluded_interfaces(field, value):
    return get_default_field_value(field, value)


def instance_metric_patterns(field, value):
    return get_default_field_value(field, value)


def instance_min_collection_interval(field, value):
    return 15


def instance_service(field, value):
    return get_default_field_value(field, value)


def instance_tags(field, value):
    return get_default_field_value(field, value)


def instance_use_sudo_conntrack(field, value):
    return True


def instance_whitelist_conntrack_metrics(field, value):
    return ['max', 'count']
