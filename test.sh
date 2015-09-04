HOST=${HOST:-localhost}
PORT=${PORT:-8085}
HOST_URL=http://$HOST:$PORT
echo using host: $HOST_URL

IPXE_BOOT_URL=$HOST_URL/coreos-ipxe/arothste/id_rsa.pub/test
echo iPXE boot url: $IPXE_BOOT_URL
curl $IPXE_BOOT_URL

IPXE_BOOT_CC_URL=$HOST_URL/coreos-cloudconfig/arothste/id_rsa.pub/test
echo iPXE cloud-config url: $IPXE_BOOT_CC_URL
curl $IPXE_BOOT_CC_URL
