HOST=${HOST:-localhost}
PORT=${PORT:-8085}
HOST_URL=http://$HOST:$PORT
echo using host: $HOST_URL
curl $HOST_URL/coreos-ipxe/arothste/id_rsa.pub/test
curl $HOST_URL/coreos-cloudconfig/arothste/id_rsa.pub/test
