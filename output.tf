output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.app_server.id
}

output "function_url" {
  value = aws_api_gateway_stage.gateway_stage.invoke_url
  }

output "Twilio_account" {
  value = var.TWILIO_ACCOUNT_SID
  }
