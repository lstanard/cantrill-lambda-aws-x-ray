#!/bin/bash

set -e

FUNCTION_NAME=lambda_function.py
BUILD_DIR=package
ZIP_NAME=lambda_function_bundle.zip

# Clean up previous build
rm -rf $BUILD_DIR $ZIP_NAME

# Create build dir and install dependencies
mkdir -p $BUILD_DIR
pip install -r requirements.txt -t $BUILD_DIR

# Copy lambda function code into build dir
cp $FUNCTION_NAME $BUILD_DIR/

# Create zip file
cd $BUILD_DIR
zip -r ../$ZIP_NAME .
cd ..

clear
echo "✅ Packaged $ZIP_NAME"
