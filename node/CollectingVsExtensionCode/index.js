var fs = require('fs');
var path = require('path');

var arrExtensionFile = [];

//解析需要遍历的文件夹，我这以E盘根目录为例
var filePath = path.resolve('C:/study/vscode/src/vs/platform/extensionManagement');

//调用文件遍历方法
fileDisplay(filePath);

/**
 * 文件遍历方法
 * @param filePath 需要遍历的文件路径
 */
function fileDisplay(filePath) {
    //根据文件路径读取文件，返回文件列表
    fs.readdir(filePath, function (err, files) {
        if (err) {
            console.warn(err)
        } else {
            //遍历读取到的文件列表
            files.forEach(function (filename) {
                //获取当前文件的绝对路径
                var filedir = path.join(filePath, filename);
                //根据文件路径获取文件信息，返回一个fs.Stats对象
                fs.stat(filedir, function (eror, stats) {
                    if (eror) {
                        console.warn('获取文件stats失败');
                    } else {
                        var isFile = stats.isFile();//是文件
                        var isDir = stats.isDirectory();//是文件夹
                        if (isFile) {
                            ReadLinebyLine(filedir);
                        }
                        if (isDir) {
                            fileDisplay(filedir);//递归，如果是文件夹，就继续遍历该文件夹下面的文件
                        }
                    }
                })
            });
        }
    });

    arrExtensionFile.sort();
    arrExtensionFile.forEach((line) => {
        console.log(line);
        var sFileName;

        var iFoundSlash = line.lastIndexOf('/');
        if (iFoundSlash == -1)
            return;
        else {
            sFileName = line.substring(iFoundSlash) + ".js"
        } 

        //console.log('./files' + sFileName);

        // fs.copyFile('C:\study\vscode\src\\' + line + '.js', '.\files\\' + sFileName, (err) => {
        //    if (err) throw err;
        //    console.log('File was copied to destination');
        //  });
    });
}

var sSearch = "import { getErrorMessage, isPromiseCanceledError, canceled } from 'vs/base/common/errors';"
//console.log(FindExtensionFile(sSearch));

function FindExtensionFile(sSearch) {
    var startPattern = /from '/i;
    var endPattern = /';/i;

    var iStart = sSearch.search(startPattern);
    var iEnd = sSearch.search(endPattern);

    var sFound = null;

    if (iStart !== -1 && iEnd !== -1) {
        sFound = sSearch.substring(iStart + 6, iEnd);
        if (arrExtensionFile.indexOf(sFound) == -1)
            arrExtensionFile.push(sFound)
    }
    return sFound;
}

function ReadLinebyLine(filedir) {
    var sSourceCode = fs.readFileSync(filedir);
    const allLines = sSourceCode.toString().split(/\r\n|\n/);
    // Reading line by line
    allLines.forEach((line) => {
        FindExtensionFile(line);
    });
}



