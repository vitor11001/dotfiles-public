use inquire::Select;
use crate::modules::exit::{ExitChoices, close_program};
use crate::constants::packages::BLUETOOTH_PACKAGES;
use crate::installations::install_from_pacman::install_from_pacman;


pub fn bluetooth_packages() {
    let install_bluetooth = vec![
        "Install bluetooth packages",
        "exit"
    ];

    let install_bluetooth_ans = Select::new(
        "Would you like to install bluetooth packages?", 
        install_bluetooth
    ).prompt();

    if let Ok(choice) = install_bluetooth_ans {
        match choice {
            "Install bluetooth packages" => install_from_pacman(BLUETOOTH_PACKAGES, "bluetooth packages"),
            "exit" => close_program(ExitChoices::Exit),
            _ => close_program(ExitChoices::InvalidChoice),
        }
    } else {
        close_program(ExitChoices::Error);
    }
}
