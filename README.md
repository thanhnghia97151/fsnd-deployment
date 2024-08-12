# Project: Capstone Project - FSND

## Getting Setup

### Python 3.7

You can follow [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

### Github Link: [FSND Project](https://github.com/thanhnghia97151/fsnd-deployment.git)

```bash
git clone https://github.com/thanhnghia97151/fsnd-deployment.git
```

### Install Dependencies

Postman - API testing tools
Render - Platform for hosting of web apps

Navigate to the /backend and run:

```bash
pip install -r requirements.txt

```

### Database Setup

From the /FSND folder in terminal run:

```bash
source setup.sh
python manage.py db init
python magage.py db migrate
python app.py

```

### Endpoints

* GET /actors and /movies
* DELETE /actors/ and /movies/
* POST /actors and /movies and
* PATCH /actors/ and /movies/

### Roles

#### Casting Assistant

* GET /actors and /movies

#### Casting Director

* GET /actors and /movies
* ADD /actors and DELETE /actors
* PATCH /actors and /movies

#### Executive Producer

* GET /actors and /movies
* ADD /actors and DELETE /actors
* PATCH /actors and /movies
* ADD /movies and DELETE /movies

### JWT Token for each user to call API

* Casting Assistant:

```bash
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlczMG1LNWpBTGh2blM5VVQ0ZXJ4YiJ9.eyJpc3MiOiJodHRwczovL3VkYWNpdHktbmdoaWEtZnVsbC1zdGFjay51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjZiOWZlNzkwYmQyYjFlN2M1NjQ4NzZjIiwiYXVkIjoiZnNuZC1pbWFnZSIsImlhdCI6MTcyMzQ3OTE4MiwiZXhwIjoxNzIzNDg2MzgyLCJzY29wZSI6IiIsImF6cCI6Ilo5MmZ0Ukd0ZGdLT1FmV0pVTmljcFBpZUJTTGlUVW1UIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.ot9qwgCD5scd-I2HF7KxQb4a7ZNA58vuVhkT2y0Q5wzSUjGhl78-7PYhIWrL6e8Qk-OtyjJueQbwPowENzYqfwb9yrVAmw7ytapCrEvHc8Iy5H2Rw1zqIUOjwQUoPFM5mkYEjOOiqjrqLl1bh8dx4Rm3JgalPprg7TDc8G875WhTs5ZNktpFiVfbfNnYwmC1yVShVk4zxMBlhBqjDrtwbogtTlzU--yEeEnFDngQuJWhhKUHEI5BQxOOjpcszsicjdDNs7NbMbWndsQcB0_en_blwh1KE0oQGMrOOH5fTTevjhomcxOl9PV-c2sqDBZW2CIXm0P6sXJ2eO3EZ7brEA

```

* Casting Director:

```bash
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlczMG1LNWpBTGh2blM5VVQ0ZXJ4YiJ9.eyJpc3MiOiJodHRwczovL3VkYWNpdHktbmdoaWEtZnVsbC1zdGFjay51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjZiOWZmNWFmZTI3Nzg1NTExNTUzYWQ3IiwiYXVkIjoiZnNuZC1pbWFnZSIsImlhdCI6MTcyMzQ3OTYxMCwiZXhwIjoxNzIzNDg2ODEwLCJzY29wZSI6IiIsImF6cCI6Ilo5MmZ0Ukd0ZGdLT1FmV0pVTmljcFBpZUJTTGlUVW1UIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDphY3RvciJdfQ.rkiJg7l0V08x1RfVSo_XSWBXiKa4YoRk3FrGdhXPbbxu-neWWjGUhCtZRpYTiphRLe4Cmtms477hp1fHkkdPPlbxzR8tgD-WYg_bgGNDA2P63IDIDf9zVz9qUWvUm5Isny3Kjs4rnkalt9UBOTGDWDEUXvZp54mxmxv6gGrIhaC83D0zoZok6cp1CEvGurK0EOs9KxTQIU3Qxypy_QP823qPLW5pTqsb68M-jbYiOXcD0eJfhh6CGc5qezmbva879cmdWDSNcIcB9fnj1AnDymeEqTOeKSYthsdPBhYKtszrvDIDWo4HqZ1wUxE5YArjaFXYp1D_h_thNaZtWJ4buw

```

* Executive Producer:

```bash
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlczMG1LNWpBTGh2blM5VVQ0ZXJ4YiJ9.eyJpc3MiOiJodHRwczovL3VkYWNpdHktbmdoaWEtZnVsbC1zdGFjay51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjZiOWZmOTEwYmQyYjFlN2M1NjQ4ODhjIiwiYXVkIjoiZnNuZC1pbWFnZSIsImlhdCI6MTcyMzQ3NzkxMiwiZXhwIjoxNzIzNDg1MTEyLCJzY29wZSI6IiIsImF6cCI6Ilo5MmZ0Ukd0ZGdLT1FmV0pVTmljcFBpZUJTTGlUVW1UIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDphY3RvciIsInBvc3Q6bW92aWUiXX0.EwpjRNcw9ZnWNny5iVLpfBaAjZQRF4LfYFukA1hMVaP594Cq_7Mu1YJoiOYgTAm1cBo9A7atwXbFVLgI9g0VDYj5OkPD103p4UnvyeN58mldxFgzMHorHM47VRewkt7Oc4rgQk1T5Bq5i0fQ3ukxYTQAK4wI3HFgppWgjsqMr87DESSHcIYvCov7Ic3Oh1u5Fj09Ic-CLXgwCij5_LgrJ4msilstsT_G-mOlOBBzlpxVwnJGtwpXM3yeJNh-8FRJ2hOs8AC2p2hMJ1TphQN_OL1vnP69Y55KmxGiLtmTN7wi_Xi58cKFogIIl4z3UXRKh31etD-Gbs-gHdrgw2R9OA

```

## API Endpoints

### Default Path

Verify hosting on Render.
Response:  

```bash
    Welcom to FSND!
```

### GET Endpoints

#### GET /movies

Response:  

```bash
{
    "movies": [
        {
            "id": 1,
            "release_date": "2024/1/1",
            "title": "Title2"
        }
    ],
    "success": true
}
```

#### GET /actors

Response:  

```bash
{
    "actors": [
        {
            "age": 31,
            "gender": "Male",
            "id": 1,
            "name": "Micheal"
        }
    ],
    "success": true
}
```

### POST Endpoints

#### POST /actor

Request:

```bash
{
    "name": "Micheal",
    "gender": "Male",
    "age": 31
}
```

Response:  

```bash
{
    "success": true
}
```

#### POST /movie

Request:

```bash
{
    "title": "Title1",
    "release_date": "2024/1/1"
}
```

Response:  

```bash
{
    "success": true
}
```

### PATCH Endpoints

#### PATCH /actor/< id >

Request:

```bash
{
    "name": "Update Micheal 1",
    "gender": "Male",
    "age": 50
}
```

Response:  

```bash
{
    "success": true
}
```

#### PATCH /movie/< id >

Request:

```bash
{
    "title": "Update Title2",
    "release_date": "2024/1/1"
}
```

Response:  

```bash
{
    "success": true
}
```

### DELETE Endpoints

#### DELETE /actor/< id >

Response:  

```bash
{
    "success": true
}
```

#### DELETE /movie/< id >

Response:  

```bash
{
    "success": true
}
```

## Run Unit Test

Navigate to the /FSND and run:

```bash
python test_fsnd.py
```
