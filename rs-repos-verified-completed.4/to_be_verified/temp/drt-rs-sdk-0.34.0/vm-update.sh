#!/bin/bash

# Locally update the VM version

VM_TAG="v1.4.53"

echo "Before:"
drtpy config dump
drtpy config set dependencies.vmtools.tag $VM_TAG
echo "After:"
drtpy config dump

drtpy deps install vmtools --overwrite
