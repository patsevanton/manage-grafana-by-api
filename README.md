# manage-grafana-by-api
Manage Grafana by API

## Requirements

You need Python 3 and only the `requests` library installed.

## Quick start

Install the pip package:

```
pip3 install -U grafana_api requests
```

And then connect to your Grafana API endpoint:

```python
from grafana_api.grafana_face import GrafanaFace

grafana_api = GrafanaFace(auth='abcde....', host='api.my-grafana-host.com')

# Search dashboards based on tag
grafana_api.search.search_dashboards(tag='applications')

# Find a user by email
user = grafana_api.users.find_user('test@test.com')

# Add user to team 2
grafana_api.teams.add_team_member(2, user["id"])

# Create or update a dashboard
grafana_api.dashboard.update_dashboard(dashboard={'dashboard': {...}, 'folderId': 0, 'overwrite': True})

# Delete a dashboard by UID
grafana_api.dashboard.delete_dashboard(dashboard_uid='abcdefgh')
```


## Authentication

There are two ways to autheticate to grafana api. Either use api token or basic auth.

To use admin API you need to use basic auth [as stated here](https://grafana.com/docs/grafana/latest/http_api/admin/)

```python
# Use basic authentication:

grafana_api = GrafanaFace(
          auth=("username","password"),
          host='api.my-grafana-host.com'
          )

# Use token
grafana_api = GrafanaFace(
          auth='abcdetoken...',
          host='api.my-grafana-host.com'
          )
```
