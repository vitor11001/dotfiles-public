use inquire::Select;
use crate::modules::exit::{ExitChoices, close_program};
use crate::constants::packages::NVIDIA_PACKAGES;
use crate::installations::install_from_pacman::install_from_pacman;


pub fn nvidia_drivers() {
    let install_nvidia = vec![
        "Install nvidia drivers",
        "exit"
    ];

    let install_nvidia_ans = Select::new(
        "Would you like to install nvidia drivers?", 
        install_nvidia
    ).prompt();

    if let Ok(choice) = install_nvidia_ans {
        match choice {
            "Install nvidia drivers" => install_from_pacman(NVIDIA_PACKAGES, "nvidia drivers"),
            "exit" => close_program(ExitChoices::Exit),
            _ => close_program(ExitChoices::InvalidChoice),
        }
    } else {
        close_program(ExitChoices::Error);
    }
}
