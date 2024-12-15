use inquire::Select;
use crate::modules::exit::{ExitChoices, close_program};
use crate::constants::packages::PIPEWIRE_PACKAGES;
use crate::installations::install_from_pacman::install_from_pacman;


pub fn pipewire_packages() {
    let install_pipewire = vec![
        "Install pipewire packages",
        "exit"
    ];

    let install_pipewire_ans = Select::new(
        "Would you like to install pipewire packages?", 
        install_pipewire
    ).prompt();

    if let Ok(choice) = install_pipewire_ans {
        match choice {
            "Install pipewire packages" => install_from_pacman(PIPEWIRE_PACKAGES, "pipewire packages"),
            "exit" => close_program(ExitChoices::Exit),
            _ => close_program(ExitChoices::InvalidChoice),
        }
    } else {
        close_program(ExitChoices::Error);
    }
}
