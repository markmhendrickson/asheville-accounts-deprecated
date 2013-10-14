## accounts.asheville

This is an [Asheville](https://github.com/asheville) internal
service for the management of user accounts.

Given proper authentication, it exposes an HTTP/JSON API for:

- Retrieving information about an Asheville user, such as authentication
tokens for their connected networks and storage systems
- Adding authentication tokens
- Deleting a user from Asheville

## Security

Initially, this API will be exposed on a local network only, requiring
the use of a VPN to be connected to by other Asheville services.

Additionally, an authentication token must be used to connect to the
service.

The authentication token is sent in the header in an `X-Asheville-Auth`
field, i.e:

```
GET: "accounts.asheville/v1/user/6f447ed6-15b5-4e3b-b301-ddc0d07f409b.json HTTP/1.1"
HOST: "accounts.asheville"
X-Asheville-Auth: "foobar-token"
```

## Hacking on asheville-accounts

`make deps` will install most of the requirements. Before you run that, though,
make sure you have libevent installed. If you don't, you'll see this error:

```
In file included from gevent/core.c:253:

gevent/libevent.h:9:10: fatal error: 'event.h' file not found

#include "event.h"
```

If you use Homebrew, you can get it with `brew install libevent`.

TODO: more Vagrant Guide

## API

### Table of Contents

- [User](#user) contains methods for manipulating individual Asheville users
- [Storages](#storages) contained methods for manipulating a storage object
- [Sources](#sources) contained methods for manipulating a source object
- [Admin](#admin) exposes various admin statistics about the Asheville userbase

This is documentation for an early API. It is very much a work-in-progress
and may change or break at any time.

### User

A user represents an invidiual that has signed up and connected at least
one storage account with Asheville.

#### Retrieve a User

**URL**: `/v1/user/<uuid>.json`

**METHOD**: `GET`

**ARGS**:

- `user_id` (required): A unique identifier representing the users
Asheville ID. This should be a 36 character UUID as specified in [RFC 4122](http://tools.ietf.org/html/rfc4122.html),
or, more realistically, generated using Python's built-in `uuid.uuid4()`

##### Example

`GET /v1/user/6f447ed6-15b5-4e3b-b301-ddc0d07f409b.json`

```json
{
    "id": "6f447ed6-15b5-4e3b-b301-ddc0d07f409b",
    "identity": {
        "name": "Jack Pearkes",
        "email": "jackpearkes@gmail.com"
    },
    "storages": [{
        "type": "dropbox",
        "authentication_type": "credential_pair",
        "access_key": "foo",
        "access_secret": "bar",
        "state": "paused",
        "settings": {
            "arbitrary": "key value settings"
        }
    }],
    "sources": [{
        "type": "facebook",
        "authentication_type": "credential_pair",
        "access_key": "foo",
        "access_secret": "bar",
        "state": "bad_authentication",
        "settings": {
            "arbitrary": "key value settings"
        },
        "content_types": {
            "photos": true,
            "checkins": false,
            "facebook_specific_thing": true
        }
    }],
    "created_at": "2013-10-05 10:33:22",
    "updated_at": "2013-10-05 10:33:22"
}
```

#### Create a User

Creates a user with the given credentials.

**URL**: `/v1/user`

**METHOD**: `POST`

**REQUEST BODY** (json):

- `identity` (optional): Identity meta data for the user
    - `name`: The users full name
    - `email`: The users email address
- `storages` (optional): An array of storage objects
    - `type` (required): The type of storage backend, i.e `dropbox`
    - `authentication_type` (required): The method of authentication, i.e `credential_pair`
    - `access_key` (required for `credential_pair` type): The key or ID on the service for the user
    - `access_secret` (required for `credential_pair` type): The secret or password associated with the key for the user on the service
    - `state` (optional): The current state of the storage backend, i.e `active` or `bad_authentication`
    - `settings` (optional): Any arbitrary service-specific settings. Any valid JSON can be passed into this key.
- `sources` (optional): An array of source objects
    - `type` (required): The type of storage backend, i.e `facebook`
    - `authentication_type` (required): The method of authentication, i.e `credential_pair`
    - `access_key` (required for `credential_pair` type): The key or ID on the service for the user
    - `access_secret` (required for `credential_pair` type): The secret or password associated with the key for the user on the service
    - `state` (optional): The current state of the storage backend, i.e `active` or `bad_authentication`
    - `settings` (optional): Any arbitrary service-specific settings. Any valid JSON can be passed into this key.
    - `content_types` (optional): A hash of boolean key-value pairs representing what the Asheville service should sync for the user

##### Example

`POST /v1/user`

Payload:

```json
{
    "identity": {
        "email": "jackpearkes@gmail.com"
    }
}
```

Returns:

```json
{
    "id": "6f447ed6-15b5-4e3b-b301-ddc0d07f409b",
    "identity": {
        "email": "jackpearkes@gmail.com",
        "name": null
    },
    "storages": [],
    "sources": [],
    "created_at": "2013-10-05 10:33:22",
    "updated_at" "2013-10-05 10:33:22"
}
```

#### Create a Storage

Creates a storage object for a user.

**URL**: `/v1/storage`

**METHOD**: `POST`

**REQUEST BODY** (json):

- `user_id` (required): The ID of the user who owns the storage object
- `type` (required): The type of storage backend, i.e `dropbox`
- `authentication_type` (required): The method of authentication, i.e `credential_pair`
- `access_key` (required for `credential_pair` type): The key or ID on the service for the user
- `access_secret` (required for `credential_pair` type): The secret or password associated with the key for the user on the service
- `state` (optional): The current state of the storage backend, i.e `active` or `bad_authentication`
- `settings` (optional): Any arbitrary service-specific settings. Any valid JSON can be passed into this key.

##### Example

`POST /v1/storage`

Payload:

```json
{
    "user_id": "6f447ed6-15b5-4e3b-b301-ddc0d07f409b",
    "type": "dropbox",
    "authentication_type": "credential_pair",
    "access_key": "",
}
```

Returns:

```json
{
    "id": "6f447ed6-15b5-4e3b-b301-ddc0d07f409b",
    "identity": {
        "email": "jackpearkes@gmail.com",
        "name": null
    },
    "storages": [],
    "sources": [],
    "created_at": "2013-10-05 10:33:22",
    "updated_at" "2013-10-05 10:33:22"
}
```

### Admin

Admin exposes various statistics about the Asheville user accounts.

#### Retrieve Stats

Returns some userbase stats about Asheville.

**URL**: `/v1/admin/stats`

**METHOD**: `GET`

##### Example

`GET /v1/admin/stats`

Returns:

```json
{
    "total_users": 41,
    "last_signup_at": "2013-10-05 10:33:22"
}
```
