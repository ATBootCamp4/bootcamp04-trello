# Fundación Jala - AT Latam Bootcamp 04

## Automation Testing Framework for Trello

This software is the confidential and propietary information of
Jalasoft, ("Confidential Information"). You shall not disclose
such Confidential Information and shall use it only in
accordance with the terms of the license agreement you entered
into with Jalasoft.

## Set up the framework on your machine

This project uses the "make" command for various actions. You can find instructions to install for git-bash [here](https://gist.github.com/evanwill/0207876c3243bbb6863e65ec5dc3f058#make).

- ### Clone project

```bash
  git clone https://github.com/ATBootCamp4/bootcamp04-trello.git
```

- ### Environment Variables

To run this project, you will need to have the following environment variables

`TRELLO_APIKEY`
`TRELLO_TOKEN`
[(get them here)](https://trello.com/app-key)

`TRELLO_USER`
`TRELLO_PASSWORD`

- ### Create a virtual env
```bash
  make env
```
- ### Start virtual environment
```bash
  source .venv/Scripts/activate
```
- ### Check code (it uses flake8)
```bash
  make check
```
- ### Run tests with a filter
```bash
  make tag_api T=<tag_name>
  make tag_gui T=<tag_name>
  make wip
```
- ### Run all tests, generate and serve allure report
```bash
  make allure-report
  make allure
```