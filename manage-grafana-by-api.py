#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from grafana_api.grafana_face import GrafanaFace

grafana_api = GrafanaFace(auth=('admin', 'admin'), host='localhost', port=3000)

# Get settings
# settings = grafana_api.admin.settings()

# Get stats
# stats = grafana_api.admin.stats()

# Create user
# user = grafana_api.admin.create_user({"name": "User", "email": "user@domain.com", "login": "user", "password": "password", "OrgId": 1})

# Change user password. Update user password for user with id 2.
# user = grafana_api.admin.change_user_password(2, "newpassword")

# Change user permissions. Set admin for user with id 2.
# user = grafana_api.admin.change_user_permissions(2, True)

# Delete user with id 2.
# user = grafana_api.admin.delete_user(2)

# Create or update a dashboard
# grafana_api.dashboard.update_dashboard(dashboard={'dashboard': {...}, 'folderId': 0, 'overwrite': True})

# Search dashboards based on tag
# grafana_api.search.search_dashboards(tag='applications')

# Find organization by name
# grafana_api.organization.find_organization('myorganization')

# Get current organization
#current_organization = grafana_api.organization.get_current_organization()

# Find a user by email
# user = grafana_api.users.find_user('test@test.com')

# Add user to team 2
# grafana_api.teams.add_team_member(2, user["id"])

# Create or update a dashboard
# grafana_api.dashboard.update_dashboard(dashboard={'dashboard': {...}, 'folderId': 0, 'overwrite': True})

# Delete a dashboard by UID
# grafana_api.dashboard.delete_dashboard(dashboard_uid='abcdefgh')




