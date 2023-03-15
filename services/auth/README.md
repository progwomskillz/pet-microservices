# Auth service
## Example env vars
```bash
APP_NAME=auth-service
APP_PORT=8001
DOCKER_SHARED_VOLUME_PATH=/docker_shared_volume/
S3_SECRETS_BUCKET=petmicroservices-secrets
BASE_DOMAIN=api.auth.petmicroservices.example.com
```
## Basic commands
`${env}` is a variable. `local` is default value. Can take the following values: `local`, `test`, `dev`, `staging`, `prod`.

For secrets files storage using AWS S3 bucket ([AWS CLI](https://aws.amazon.com/cli/) needed).
##### push secrets to AWS S3 bucket
```bash
make push_secrets ENV=${env}
```
Will push your local secrets files to remote AWS S3 bucket.
Will push files only from `secrets/${env}` folder!
##### pull secrets from AWS S3 bucket
```bash
make pull_secrets ENV=${env}
```
Will pull remote secrets files from AWS S3 bucket to local machine.
Will pull files only for `${env}` env and stage in `/secrets/${env}`!
##### run microservice
```bash
make up_containers ENV=${env}
```
##### run tests
```bash
make tests ENV=${env}
```
