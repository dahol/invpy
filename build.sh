


while getopts b:p: flag
do
    case "${flag}" in
        b) build=${OPTARG};;
        p) push=${OPTARG};;
    esac
done

# Build

if [ "$build" = "true" ] ; then
    echo "Building.."
    docker build . -t dahol/invpy:latest
    echo "Done building!"
    elif [ "$build" = "false" ] ; then
    echo "Skipping build.."
fi

# Push

if [ "$push" = "true" ] ; then
    echo "Pushing.."
    docker push dahol/invpy:latest
    echo "Done pushing!"
    elif [ "$push" = "false" ] ; then
    echo "Skipping push.."
fi