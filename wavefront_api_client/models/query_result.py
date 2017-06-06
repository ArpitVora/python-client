# coding: utf-8

"""
    Wavefront Public API

    <p>Wavefront public APIs enable you to interact with Wavefront servers using standard web service API tools. You can use the APIs to automate commonly executed operations such as automatically tagging sources.</p><p>When you make API calls outside the Wavefront UI you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p><p>For legacy versions of the Wavefront API, see the <a href=\"/api-docs/ui/deprecated\">legacy API documentation</a>.</p>

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class QueryResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, query=None, name=None, skip=None, stats=None, warnings=None, metrics_used=None, hosts_used=None, host_tags_used=None, granularity=None, num_compilation_tasks=None, query_keys=None, raw_points_stats=None, summarized_points_stats=None, timeseries=None, events=None):
        """
        QueryResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'query': 'str',
            'name': 'str',
            'skip': 'int',
            'stats': 'StatsModel',
            'warnings': 'str',
            'metrics_used': 'list[str]',
            'hosts_used': 'list[str]',
            'host_tags_used': 'list[str]',
            'granularity': 'int',
            'num_compilation_tasks': 'int',
            'query_keys': 'list[QueryKeyContainer]',
            'raw_points_stats': 'list[TimeseriesStatsContainer]',
            'summarized_points_stats': 'list[TimeseriesStatsContainer]',
            'timeseries': 'list[Timeseries]',
            'events': 'list[ReportEvent]'
        }

        self.attribute_map = {
            'query': 'query',
            'name': 'name',
            'skip': 'skip',
            'stats': 'stats',
            'warnings': 'warnings',
            'metrics_used': 'metricsUsed',
            'hosts_used': 'hostsUsed',
            'host_tags_used': 'hostTagsUsed',
            'granularity': 'granularity',
            'num_compilation_tasks': 'numCompilationTasks',
            'query_keys': 'queryKeys',
            'raw_points_stats': 'rawPointsStats',
            'summarized_points_stats': 'summarizedPointsStats',
            'timeseries': 'timeseries',
            'events': 'events'
        }

        self._query = query
        self._name = name
        self._skip = skip
        self._stats = stats
        self._warnings = warnings
        self._metrics_used = metrics_used
        self._hosts_used = hosts_used
        self._host_tags_used = host_tags_used
        self._granularity = granularity
        self._num_compilation_tasks = num_compilation_tasks
        self._query_keys = query_keys
        self._raw_points_stats = raw_points_stats
        self._summarized_points_stats = summarized_points_stats
        self._timeseries = timeseries
        self._events = events

    @property
    def query(self):
        """
        Gets the query of this QueryResult.
        The query string used to obtain this result

        :return: The query of this QueryResult.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this QueryResult.
        The query string used to obtain this result

        :param query: The query of this QueryResult.
        :type: str
        """

        self._query = query

    @property
    def name(self):
        """
        Gets the name of this QueryResult.
        The name of this query

        :return: The name of this QueryResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this QueryResult.
        The name of this query

        :param name: The name of this QueryResult.
        :type: str
        """

        self._name = name

    @property
    def skip(self):
        """
        Gets the skip of this QueryResult.
        Unused/deprecated

        :return: The skip of this QueryResult.
        :rtype: int
        """
        return self._skip

    @skip.setter
    def skip(self, skip):
        """
        Sets the skip of this QueryResult.
        Unused/deprecated

        :param skip: The skip of this QueryResult.
        :type: int
        """

        self._skip = skip

    @property
    def stats(self):
        """
        Gets the stats of this QueryResult.
        Statistics about the result data

        :return: The stats of this QueryResult.
        :rtype: StatsModel
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """
        Sets the stats of this QueryResult.
        Statistics about the result data

        :param stats: The stats of this QueryResult.
        :type: StatsModel
        """

        self._stats = stats

    @property
    def warnings(self):
        """
        Gets the warnings of this QueryResult.
        The warnings incurred by this query

        :return: The warnings of this QueryResult.
        :rtype: str
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """
        Sets the warnings of this QueryResult.
        The warnings incurred by this query

        :param warnings: The warnings of this QueryResult.
        :type: str
        """

        self._warnings = warnings

    @property
    def metrics_used(self):
        """
        Gets the metrics_used of this QueryResult.

        :return: The metrics_used of this QueryResult.
        :rtype: list[str]
        """
        return self._metrics_used

    @metrics_used.setter
    def metrics_used(self, metrics_used):
        """
        Sets the metrics_used of this QueryResult.

        :param metrics_used: The metrics_used of this QueryResult.
        :type: list[str]
        """

        self._metrics_used = metrics_used

    @property
    def hosts_used(self):
        """
        Gets the hosts_used of this QueryResult.

        :return: The hosts_used of this QueryResult.
        :rtype: list[str]
        """
        return self._hosts_used

    @hosts_used.setter
    def hosts_used(self, hosts_used):
        """
        Sets the hosts_used of this QueryResult.

        :param hosts_used: The hosts_used of this QueryResult.
        :type: list[str]
        """

        self._hosts_used = hosts_used

    @property
    def host_tags_used(self):
        """
        Gets the host_tags_used of this QueryResult.

        :return: The host_tags_used of this QueryResult.
        :rtype: list[str]
        """
        return self._host_tags_used

    @host_tags_used.setter
    def host_tags_used(self, host_tags_used):
        """
        Sets the host_tags_used of this QueryResult.

        :param host_tags_used: The host_tags_used of this QueryResult.
        :type: list[str]
        """

        self._host_tags_used = host_tags_used

    @property
    def granularity(self):
        """
        Gets the granularity of this QueryResult.

        :return: The granularity of this QueryResult.
        :rtype: int
        """
        return self._granularity

    @granularity.setter
    def granularity(self, granularity):
        """
        Sets the granularity of this QueryResult.

        :param granularity: The granularity of this QueryResult.
        :type: int
        """

        self._granularity = granularity

    @property
    def num_compilation_tasks(self):
        """
        Gets the num_compilation_tasks of this QueryResult.

        :return: The num_compilation_tasks of this QueryResult.
        :rtype: int
        """
        return self._num_compilation_tasks

    @num_compilation_tasks.setter
    def num_compilation_tasks(self, num_compilation_tasks):
        """
        Sets the num_compilation_tasks of this QueryResult.

        :param num_compilation_tasks: The num_compilation_tasks of this QueryResult.
        :type: int
        """

        self._num_compilation_tasks = num_compilation_tasks

    @property
    def query_keys(self):
        """
        Gets the query_keys of this QueryResult.

        :return: The query_keys of this QueryResult.
        :rtype: list[QueryKeyContainer]
        """
        return self._query_keys

    @query_keys.setter
    def query_keys(self, query_keys):
        """
        Sets the query_keys of this QueryResult.

        :param query_keys: The query_keys of this QueryResult.
        :type: list[QueryKeyContainer]
        """

        self._query_keys = query_keys

    @property
    def raw_points_stats(self):
        """
        Gets the raw_points_stats of this QueryResult.

        :return: The raw_points_stats of this QueryResult.
        :rtype: list[TimeseriesStatsContainer]
        """
        return self._raw_points_stats

    @raw_points_stats.setter
    def raw_points_stats(self, raw_points_stats):
        """
        Sets the raw_points_stats of this QueryResult.

        :param raw_points_stats: The raw_points_stats of this QueryResult.
        :type: list[TimeseriesStatsContainer]
        """

        self._raw_points_stats = raw_points_stats

    @property
    def summarized_points_stats(self):
        """
        Gets the summarized_points_stats of this QueryResult.

        :return: The summarized_points_stats of this QueryResult.
        :rtype: list[TimeseriesStatsContainer]
        """
        return self._summarized_points_stats

    @summarized_points_stats.setter
    def summarized_points_stats(self, summarized_points_stats):
        """
        Sets the summarized_points_stats of this QueryResult.

        :param summarized_points_stats: The summarized_points_stats of this QueryResult.
        :type: list[TimeseriesStatsContainer]
        """

        self._summarized_points_stats = summarized_points_stats

    @property
    def timeseries(self):
        """
        Gets the timeseries of this QueryResult.
        The time series data for this query

        :return: The timeseries of this QueryResult.
        :rtype: list[Timeseries]
        """
        return self._timeseries

    @timeseries.setter
    def timeseries(self, timeseries):
        """
        Sets the timeseries of this QueryResult.
        The time series data for this query

        :param timeseries: The timeseries of this QueryResult.
        :type: list[Timeseries]
        """

        self._timeseries = timeseries

    @property
    def events(self):
        """
        Gets the events of this QueryResult.
        The events occurring during this time span

        :return: The events of this QueryResult.
        :rtype: list[ReportEvent]
        """
        return self._events

    @events.setter
    def events(self, events):
        """
        Sets the events of this QueryResult.
        The events occurring during this time span

        :param events: The events of this QueryResult.
        :type: list[ReportEvent]
        """

        self._events = events

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, QueryResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
