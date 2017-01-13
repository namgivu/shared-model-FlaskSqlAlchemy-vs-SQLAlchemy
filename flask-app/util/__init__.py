def get_param(request, name, required=False):
  param = request.values.get(name)

  if required: #param is required - raise error when not provided in `request`
    if not param:
      raise Exception("Param '{name}' is required".format(name=name) )

  return param