# Copyright 2020-present Open Networking Foundation
# Original copyright 2020-present ADTRAN, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and

# set default shell
SHELL = bash -e -o pipefail

ROOT_DIR  := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

# Variables
VERSION   ?= $(shell cat ./VERSION)
LINT_ARGS ?= --verbose --configure LineTooLong:130 -e LineTooLong \
             --configure TooManyTestSteps:60 -e TooManyTestSteps \
             --configure TooManyTestCases:50 -e TooManyTestCases \
             --configure TooFewTestSteps:1 \
             --configure TooFewKeywordSteps:1 \
             --configure FileTooLong:1500 -e FileTooLong \
             -e TrailingWhitespace

ROBOT_FILES  := $(shell find . -name test.robot -print)
DMI_SERVER_FILE ?= $(ROOT_DIR)/tests/servers/dmi/dmi_server.py

# For each makefile target, add ## <description> on the target line and it will be listed by 'make help'
help: ## Print help for each Makefile target
	@echo "Usage: make [<target>]"
	@echo "where available targets are:"
	@echo
	@grep '^[[:alpha:]_-]*:.* ##' $(MAKEFILE_LIST) \
		| sort | awk 'BEGIN {FS=":.* ## "}; {printf "%-25s : %s\n", $$1, $$2};'

vst_venv:
	virtualenv -p python3 $@ ;\
	source ./$@/bin/activate ;\
	python -m pip install -r requirements.txt
	python $(DMI_SERVER_FILE) & echo $$! > server.PID

test: vst_venv
	source ./$</bin/activate ; set -u ;\
    rflint $(LINT_ARGS) $(ROBOT_FILES)

clean:
	find . -name output.xml -print

clean-all: clean
	rm -rf vst_venv
	kill `cat server.PID` && rm server.PID

# end file