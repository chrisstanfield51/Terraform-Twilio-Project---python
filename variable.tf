variable "instance_name" {
  description = "Value of the Name tag for the EC2 instance"
  type        = string
  default     = "TestInstance"
}

variable "myregion" {
  description = "Region"
  type        = string
  default     = "us-west-2"
}

variable "TWILIO_ACCOUNT_SID" {
    type        = string
    description = "Variable for TWILIO API info"
    default     = "Empty"
}

variable "TWILIO_AUTH_TOKEN" {
    type        = string
    description = "Variable for TWILIO API info"
    default     = "Empty"
}

variable "TWILIO_PHONE" {
    type        = string
    description = "Variable for TWILIO API info"
    default     = "Empty"
}
