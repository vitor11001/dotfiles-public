// use std::process::Command;


// pub fn install_from_pacman(packages: &[&str], name_packages_install: &str) {
//     println!("Installing {}", name_packages_install);

//     let mut command = Command::new("sudo");
//     command.arg("pacman")
//            .arg("-S")
//            .arg("--needed")
//            .arg("--noconfirm");

//     for package in packages.iter() {
//         command.arg(package);
//     }

//     let output = command.output().expect("Failed to execute command");

//     if output.status.success() {
//         let stdout = String::from_utf8_lossy(&output.stdout);
//         println!("Output: {}", stdout);
//     } else {
//         let stderr = String::from_utf8_lossy(&output.stderr);
//         eprintln!("Error: {}", stderr);
//     }

// }
use std::process::{Command, Stdio};
use std::io::{self, BufRead};

pub fn install_from_pacman(packages: &[&str], name_packages_install: &str) {
    println!("Installing {}", name_packages_install);

    let mut command = Command::new("sudo");
    command.arg("pacman")
           .arg("-S")
           .arg("--needed")
           .arg("--noconfirm");

    for package in packages.iter() {
        command.arg(package);
    }

    // Redireciona stdout e stderr para o terminal
    command.stdout(Stdio::piped());
    command.stderr(Stdio::piped());

    let mut child = command.spawn().expect("Failed to execute command");

    // Captura stdout
    if let Some(stdout) = child.stdout.take() {
        let reader = io::BufReader::new(stdout);
        for line in reader.lines() {
            if let Ok(line) = line {
                println!("{}", line);
            }
        }
    }

    // Captura stderr
    if let Some(stderr) = child.stderr.take() {
        let reader = io::BufReader::new(stderr);
        for line in reader.lines() {
            if let Ok(line) = line {
                eprintln!("{}", line);
            }
        }
    }

    let output = child.wait().expect("Failed to wait on child");

    if !output.success() {
        eprintln!("Command failed with status: {}", output);
    }
}
