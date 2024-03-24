# Project Manager

## Para empezar

### Requisitos

- NVM (recomendado para asegurar versión de node) ver [documentación oficial](https://github.com/nvm-sh/nvm?tab=readme-ov-file#installing-and-updating)

```sh
 nvm use
 # o
 nvm use <version>
```

> Si quieres automatizar el proceso, puedes crear un script siguiendo la [documentación oficial](https://github.com/nvm-sh/nvm?tab=readme-ov-file#calling-nvm-use-automatically-in-a-directory-with-a-nvmrc-file)

<details>
	<summary>Pequeño script de automatización</summary>
	
- For Linux/MacOS:
	```sh
	# .bashrc | .zshrc | cualquier archivo de configuración
	# pequeño script para cambiar de version al entrar al directorio
	cd() {
  builtin cd "$@"
		if [[ -f .nvmrc ]]; then
			nvm use > /dev/null
			# Si quieres que te diga la versión
			nvm use
		fi
	}
	```

- For Windows:

  ```powershell
  # $PROFILE
  function Change-Node-Version {
  	param($path)
  	& Set-Location $path
  	$pwd = pwd
  	if ( Test-Path "$pwd\\.nvmrc" ) {
  		$version = Get-Content .nvmrc
  		nvm use $version
  	}
  }
  New-Alias -Name cd -Value Change-Node-Version -Force -Option AllScope
  ```

  </details>

- PNPM (es nuestra recomendación por su eficiencia y rapidez)

  ```sh
  npm install -g pnpm
  ```

- o NPM

  ```sh
  npm install npm@latest -g
  ```

### Instalación

1. Clona el repositorio

   ```sh
   git clone https://github.com/luisangelponcealvarez/Password-Manager.git
   ```

2. Instala los paquetes de NPM

   ```sh
   pnpm install
   ```

3. Ejecuta el proyecto

   ```sh
   pnpm run dev
   ```

## Contribuir al proyecto

Las contribuciones son lo que hacen que la comunidad de código abierto sea un lugar increíble para aprender, inspirar y crear. ¡Cualquier contribución que hagas es **muy apreciada**!

Si tienes alguna sugerencia que podría mejorar el proyecto, por favor haz un [_fork_](https://github.com/luisangelponcealvarez/Password-Manager/fork) del repositorio y crea una [_pull request_](https://github.com/luisangelponcealvarez/Password-Manager/pulls). También puedes simplemente abrir un [_issue_](https://github.com/luisangelponcealvarez/Password-Manager/issues) con la etiqueta "enhancement".

Aquí tienes una guía rápida:

1. Haz un [_fork_](https://github.com/luisangelponcealvarez/Password-Manager/fork) del Proyecto
2. Clona tu [_fork_](https://github.com/luisangelponcealvarez/Password-Manager/fork) (`git clone <URL del fork>`)
3. Añade el repositorio original como remoto (`git remote add upstream <URL del repositorio original>`)
4. Crea tu Rama de Funcionalidad (`git switch -c feature/CaracteristicaIncreible`)
5. Realiza tus Cambios (`git commit -m 'Add: alguna CaracterísticaIncreible'`)
6. Haz Push a la Rama (`git push origin feature/CaracteristicaIncreible`)
7. Abre una [_pull request_](https://github.com/luisangelponcealvarez/Password-Manager/pulls)

Por favor, consulta nuestra [guía de contribución](https://github.com/luisangelponcealvarez/Password-Manager/blob/main/CONTRIBUTING.md) para saber cómo puedes empezar de la mejor manera y siguiendo [buenas prácticas](https://github.com/luisangelponcealvarez/Password-Manager/blob/main/CONTRIBUTING.md#buenas-prácticas-).

## 🛠️ Stack

- [ElectroJs] - Framework para crear aplicaciones web.
- [Typescript] - JavaScript with syntax for types.
- [TailwindCSS] - A utility-first CSS framework for rapidly building custom designs.
- [React] - JavaScript library for building user interfaces.
