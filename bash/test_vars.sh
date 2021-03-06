if [ -z "${VAR}" ]; then
    echo "VAR is unset or set to the empty string"
fi
if [ -z "${VAR+set}" ]; then
    echo "VAR is unset"
fi
if [ -z "${VAR-unset}" ]; then
    echo "VAR is set to the empty string"
fi
if [ -n "${VAR}" ]; then
    echo "VAR is set to a non-empty string"
fi
if [ -n "${VAR+set}" ]; then
    echo "VAR is set, possibly to the empty string"
fi
if [ -n "${VAR-unset}" ]; then
    echo "VAR is either unset or set to a non-empty string"
fi

#-----------------------+-------+-------+-----------+
#               VAR is: | unset | empty | non-empty |
#-----------------------+-------+-------+-----------+
# [ -z "${VAR}" ]       | true  | true  | false     |
# [ -z "${VAR+set}" ]   | true  | false | false     |
# [ -z "${VAR-unset}" ] | false | true  | false     |
# [ -n "${VAR}" ]       | false | false | true      |
# [ -n "${VAR+set}" ]   | false | true  | true      |
# [ -n "${VAR-unset}" ] | true  | false | true      |
#-----------------------+-------+-------+-----------+