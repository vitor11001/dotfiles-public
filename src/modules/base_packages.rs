use inquire::Select;
use crate::modules::exit::{ExitChoices, close_program};
use crate::constants::packages::BASE_PACKAGES;
use crate::installations::install_from_pacman::install_from_pacman;


pub fn base_packages() {
    let install_base = vec![
        "Install base packages",
        "exit"
    ];

    let install_base_ans = Select::new(
        "Would you like to install base packages?", 
        install_base
    ).prompt();

    if let Ok(choice) = install_base_ans {
        match choice {
            "Install base packages" => install_from_pacman(BASE_PACKAGES, "base packages"),
            "exit" => close_program(ExitChoices::Exit),
            _ => close_program(ExitChoices::InvalidChoice),
        }
    } else {
        close_program(ExitChoices::Error);
    }
}
