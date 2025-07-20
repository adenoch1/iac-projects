// variables.tf

// The CIDR block for our VPC
variable "vpc_cidr" {
  type    = string
  default = "10.0.0.0/16"
}

// List of public subnet CIDRs
variable "public_subnets" {
  type    = list(string)
  default = ["10.0.1.0/24", "10.0.2.0/24"]
}

// AWS region to deploy into
variable "aws_region" {
  type    = string
  default = "us-east-1"
}
