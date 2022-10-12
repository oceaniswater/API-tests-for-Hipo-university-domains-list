"""
Execute API call with valid required parameters

1. For GET requests, verify there is NO STATE CHANGE in the system (idempotence)

2. For POST, DELETE, PATCH, PUT operations
– Ensure action has been performed correctly in the system by:
– Performing appropriate GET request and inspecting response
– Refreshing the UI in the web application and verifying new state (only applicable to manual testing)
"""