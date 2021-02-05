# test-task-SBER
chat bot MVP

## Build
```shell script
docker build -t booking_app .
```

## Run
```shell script
docker run booking_app
```
then go to `@SBERRestaurantBookingBot` in telegram and chat)

## Test

```shell script
docker run --entrypoint pytest booking_app
```
