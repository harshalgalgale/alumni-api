variable project {
  type        = string
  description = "The Google Cloud Platform project name"
  default = "alumni-dascaet-rahuri"
}

variable service {
  description = "Name of the service"
  type        = string
  default = "alumni-api"
}

variable region {
  default = "europe-west2"
  type    = string
}

variable instance_name {
  description = "Name of the postgres instance (PROJECT_ID:REGION:INSTANCE_NAME))"
  type        = string
  default = "alumni-dascaet-rahuri:europe-west2:alumni-db-psql"
}