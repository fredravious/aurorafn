def create(code, numericCode, message, service, intent="prod", Vars=None):
	return {
		"errorCode":code,
		"errorMessage":message,
		"messageVars":Vars,
		"numericErrorCode":numericCode,
		"originatingService":service,
		"intent":intent
	}
	
def method(service, intent):
	return create(
		'errors.com.epicgames.common.method_not_allowed',
		1009,
		'Sorry the resource you were trying to access cannot be accessed with the HTTP method you used.',
		service, intent
	)
	
def permission(permission, Type, service, intent):
	return create(
		'errors.com.epicgames.common.missing_permission',
		1023,
		f'Sorry your login does not posses the permissions \'{permission} {Type}\' needed to perform the requested operation',
		service, intent, [permission, Type]
	)