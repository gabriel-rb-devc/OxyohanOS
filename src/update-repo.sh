#!/bin/bash
set -e

echo "A gerar o indice Packages..."
apt-ftparchive packages dists/stable/main/binary-amd64/ > dists/stable/main/binary-amd64/Packages
gzip -k -f dists/stable/main/binary-amd64/Packages

echo "A gerar o ficheiro Release..."
apt-ftparchive -o APT::FTPArchive::Release::Origin="OxyohanOS" \
               -o APT::FTPArchive::Release::Label="OxyohanOS" \
               -o APT::FTPArchive::Release::Suite="stable" \
               -o APT::FTPArchive::Release::Codename="stable" \
               -o APT::FTPArchive::Release::Architectures="amd64" \
               -o APT::FTPArchive::Release::Components="main" \
               release dists/stable/ > dists/stable/Release

echo "Pronto! Agora podes fazer git add, commit e push."