FROM mcr.microsoft.com/dotnet/core/sdk:latest AS build-env
WORKDIR /app

# Copy csproj and restore as distinct layers
COPY webcalc-square.csproj ./
RUN dotnet restore

# Copy everything else and build
COPY . ./
RUN dotnet publish -c Release -o out

# Build runtime image
FROM mcr.microsoft.com/dotnet/core/aspnet:latest
WORKDIR /app
COPY --from=build-env /app/out .

EXPOSE 5001
ENTRYPOINT ["dotnet", "webcalc-square.dll"]
