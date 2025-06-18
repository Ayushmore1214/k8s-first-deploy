provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_storage_bucket" "github_backup" {
  name     = var.bucket_name
  location = var.region
}

resource "google_sql_database_instance" "pg_instance" {
  name             = "github-backup-db"
  database_version = "POSTGRES_14"
  region           = var.region

  settings {
    tier = "db-f1-micro"
  }
}

resource "google_sql_database" "backup" {
  name     = "backup"
  instance = google_sql_database_instance.pg_instance.name
}

# You’ll add secret manager, Cloud Run, IAM policies etc. here in the next iteration.
