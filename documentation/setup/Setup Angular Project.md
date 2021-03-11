# Setup Angular Project
## Prerequisites
* NodeJs installed
* NPM installed
* AngularCLI installed
* Test

## Create a new Project
* Create a new project with `ng new <name>`

* Choose **strict typing**, **routing**, and **css**

## Add angular materials ui to the project
* In the project folder use: `ng add @angular/material`

* Choose **Indigo/Pink** as the theme

* Say yes to **global typography styles**

* Say yes to **browser animations**

* Create a new shared module that contains all material modules from angular material
  
  * In the project folder use: `ng generate module shared` to create the shared module with the angular cli

  * Open the **shared.module.ts** file and replace the content with the following lines:

    ```typescript
    import { NgModule } from '@angular/core';
    import { CommonModule } from '@angular/common';

    // Material Form Controls
    import { MatAutocompleteModule } from '@angular/material/autocomplete';
    import { MatCheckboxModule } from '@angular/material/checkbox';
    import { MatDatepickerModule } from '@angular/material/datepicker';
    import { MatFormFieldModule } from '@angular/material/form-field';
    import { MatInputModule } from '@angular/material/input';
    import { MatRadioModule } from '@angular/material/radio';
    import { MatSelectModule } from '@angular/material/select';
    import { MatSliderModule } from '@angular/material/slider';
    import { MatSlideToggleModule } from '@angular/material/slide-toggle';

    // Material Navigation
    import { MatMenuModule } from '@angular/material/menu';
    import { MatSidenavModule } from '@angular/material/sidenav';
    import { MatToolbarModule } from '@angular/material/toolbar';

    // Material Layout
    import { MatCardModule } from '@angular/material/card';
    import { MatDividerModule } from '@angular/material/divider';
    import { MatExpansionModule } from '@angular/material/expansion';
    import { MatGridListModule } from '@angular/material/grid-list';
    import { MatListModule } from '@angular/material/list';
    import { MatStepperModule } from '@angular/material/stepper';
    import { MatTabsModule } from '@angular/material/tabs';
    import { MatTreeModule } from '@angular/material/tree';

    // Material Buttons & Indicators
    import { MatButtonModule } from '@angular/material/button';
    import { MatButtonToggleModule } from '@angular/material/button-toggle';
    import { MatBadgeModule } from '@angular/material/badge';
    import { MatChipsModule } from '@angular/material/chips';
    import { MatIconModule } from '@angular/material/icon';
    import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
    import { MatProgressBarModule } from '@angular/material/progress-bar';
    import { MatRippleModule } from '@angular/material/core';

    // Material Popups & Modals
    import { MatBottomSheetModule } from '@angular/material/bottom-sheet';
    import { MatDialogModule } from '@angular/material/dialog';
    import { MatSnackBarModule } from '@angular/material/snack-bar';
    import { MatTooltipModule } from '@angular/material/tooltip';

    // Material Data tables
    import { MatPaginatorModule } from '@angular/material/paginator';
    import { MatSortModule } from '@angular/material/sort';
    import { MatTableModule } from '@angular/material/table';

    const exportedModules = [
      MatAutocompleteModule,
      MatCheckboxModule,
      MatDatepickerModule,
      MatFormFieldModule,
      MatInputModule,
      MatRadioModule,
      MatSelectModule,
      MatSliderModule,
      MatSlideToggleModule,
      MatMenuModule,
      MatSidenavModule,
      MatToolbarModule,
      MatCardModule,
      MatDividerModule,
      MatExpansionModule,
      MatGridListModule,
      MatListModule,
      MatStepperModule,
      MatTabsModule,
      MatTreeModule,
      MatButtonModule,
      MatButtonToggleModule,
      MatBadgeModule,
      MatChipsModule,
      MatIconModule,
      MatProgressSpinnerModule,
      MatProgressBarModule,
      MatRippleModule,
      MatBottomSheetModule,
      MatDialogModule,
      MatSnackBarModule,
      MatTooltipModule,
      MatPaginatorModule,
      MatSortModule,
      MatTableModule
    ]

    @NgModule({
      declarations: [],
      imports: [
        CommonModule,
        exportedModules
      ],
      exports: [
        exportedModules
      ]
    })
    export class SharedModule { }
    ```

  * Open the **app.module.ts**
  file and add following lines to import the shared module properly:

    ```typescript
      import { SharedModule } from './shared/shared.module';

      @NgModule({
        imports: [
          SharedModule
        ]
      })

    ```

* Replace the content of the **app.component.html** file with the following lines to test if the angular material ui is working properly. These lines will add components from the material ui such as a toolbar, some buttons and a matcard as well as dividers:
  
  ```html
  <mat-toolbar color="primary">My Toolbar</mat-toolbar>
  <mat-divider></mat-divider>
  <h3>Basic Buttons</h3>
  <div class="example-button-row">
    <button mat-button>Basic</button>
    <button mat-button color="primary">Primary</button>
    <button mat-button color="accent">Accent</button>
    <button mat-button color="warn">Warn</button>
    <button mat-button disabled>Disabled</button>
    <a mat-button routerLink=".">Link</a>
  </div>

  <h3>Raised Buttons</h3>
  <div class="example-button-row">
    <button mat-raised-button>Basic</button>
    <button mat-raised-button color="primary">Primary</button>
    <button mat-raised-button color="accent">Accent</button>
    <button mat-raised-button color="warn">Warn</button>
    <button mat-raised-button disabled>Disabled</button>
    <a mat-raised-button routerLink=".">Link</a>
  </div>

  <h3>Stroked Buttons</h3>
  <div class="example-button-row">
    <button mat-stroked-button>Basic</button>
    <button mat-stroked-button color="primary">Primary</button>
    <button mat-stroked-button color="accent">Accent</button>
    <button mat-stroked-button color="warn">Warn</button>
    <button mat-stroked-button disabled>Disabled</button>
    <a mat-stroked-button routerLink=".">Link</a>
  </div>

  <h3>Flat Buttons</h3>
  <div class="example-button-row">
    <button mat-flat-button>Basic</button>
    <button mat-flat-button color="primary">Primary</button>
    <button mat-flat-button color="accent">Accent</button>
    <button mat-flat-button color="warn">Warn</button>
    <button mat-flat-button disabled>Disabled</button>
    <a mat-flat-button routerLink=".">Link</a>
  </div>

  <h3>Icon Buttons</h3>
  <div class="example-button-row">
    <button mat-icon-button aria-label="Example icon-button with a heart icon">
      <mat-icon>favorite</mat-icon>
    </button>
    <button mat-icon-button color="primary" aria-label="Example icon-button with a heart icon">
      <mat-icon>favorite</mat-icon>
    </button>
    <button mat-icon-button color="accent" aria-label="Example icon-button with a heart icon">
      <mat-icon>favorite</mat-icon>
    </button>
    <button mat-icon-button color="warn" aria-label="Example icon-button with a heart icon">
      <mat-icon>favorite</mat-icon>
    </button>
    <button mat-icon-button disabled aria-label="Example icon-button with a heart icon">
      <mat-icon>favorite</mat-icon>
    </button>
  </div>

  <h3>Fab Buttons</h3>
  <div class="example-button-row">
    <button mat-fab>Basic</button>
    <button mat-fab color="primary">Primary</button>
    <button mat-fab color="accent">Accent</button>
    <button mat-fab color="warn">Warn</button>
    <button mat-fab disabled>Disabled</button>
    <button mat-fab aria-label="Example icon-button with a heart icon">
      <mat-icon>favorite</mat-icon>
    </button>
    <a mat-fab routerLink=".">Link</a>
  </div>

  <h3>Mini Fab Buttons</h3>
  <div class="example-button-row">
    <button mat-mini-fab>Basic</button>
    <button mat-mini-fab color="primary">Primary</button>
    <button mat-mini-fab color="accent">Accent</button>
    <button mat-mini-fab color="warn">Warn</button>
    <button mat-mini-fab disabled>Disabled</button>
    <button mat-mini-fab aria-label="Example icon-button with a heart icon">
      <mat-icon>favorite</mat-icon>
    </button>
    <a mat-mini-fab routerLink=".">Link</a>
  </div>
  <mat-divider></mat-divider>
  <mat-card>My Card</mat-card>
  ```

## Serve and test the application
* In the project folder type `ng serve` and wait for the project to compile

* Open a browser and go to `http://localhost:4200`

* You should see a toolbar, some buttons and a matcard.

## Build the application
* Use the command `ng build --prod` in the project folder to build the project.

* The files consisting of **html**, **css** and **javascript** should now be in the /dist/ folder.

* You can use these files to deploy your application anywhere. 

* *Note*: Sometimes you need to modify some things if you use angular routing and want to deploy the dist-folder. For example use the line `<base href="/">` in your **index.html** folder.

## Setup a repository on github
### Prerequisites
* Account on github
* Git installed on your machine
* Already created empty repository on github
### Initialize local repository
* You should already have a local git repository initialized when having git installed and using `ng new <name>` without the `--skipGit` option
  
* If you still need to initialize a git repository do `git init` 
  
* Stage every file with `git add *`

* Commit your staged files with `git commit -m "Commit-Message"`

* Configure a remote repository (your github repository) with `git remote add origin <server>`. As an example i used `git remote add origin https://github.com/Akk4r1n/AngularMaterialTemplate.git` to initialize this repository as my remote one

* Now push every commit to your remote repository (the repository on github) with the command `git push origin main`. *Note*: Github initializes new repositories with the **main** branch. Your local branch could still be **master**. To rename your local branch do `git branch -m master main`.

* To configure your remote branch permanently use `git --set-upstream origin main`. After this you can do `git pull` and `git push` without specifying the remote branch each time
