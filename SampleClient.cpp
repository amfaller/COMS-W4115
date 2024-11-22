// SampleClient.cpp
//
// A sample C++ client for this NVP compiler.

#include "./tinyxml2/tinyxml2.h"
#include <iostream>
#include <fstream>

using namespace tinyxml2;

void readXml(const std::string& file)
{
    XMLDocument doc;

    if (doc.LoadFile(file.c_str()) != XML_SUCCESS)
    {
        std::cerr << "Error loading file: " << file << std::endl;
        return;
    }

    XMLElement* test = doc.FirstChildElement("test");
    if (test)
    {
        XMLElement* ThisIsAnInteger = test->FirstChildElement("ThisIsAnInteger");

        if (ThisIsAnInteger && ThisIsAnInteger->Attribute("type", "int"))
        {
            int value = std::stoi(ThisIsAnInteger->GetText());
            std::cout << "test.ThisIsAnInteger: " << value << std::endl;
        }
    }

    XMLElement* second = doc.FirstChildElement("second");
    if (second)
    {
        XMLElement* Identifier = second->FirstChildElement("Identifier");

        if (Identifier && Identifier->Attribute("type", "float"))
        {
            float value = std::stof(Identifier->GetText());
            std::cout << "second.Identifier: " << value << std::endl;
        }
    }

    XMLElement* MyNvp = doc.FirstChildElement("MyNvp");
    if (MyNvp)
    {
        XMLElement* enableSomeFunctionality = MyNvp->FirstChildElement("enableSomeFunctionality");

        if (enableSomeFunctionality && enableSomeFunctionality->Attribute("type", "bool"))
        {
            bool value = enableSomeFunctionality->GetText();
            std::cout << "MyNvp.enableSomeFunctionality: " << value << std::endl;
        }
    }

    XMLElement* Hey = doc.FirstChildElement("Hey");
    if (Hey)
    {
        XMLElement* ThisOneIsAString = Hey->FirstChildElement("ThisOneIsAString");

        if (ThisOneIsAString && ThisOneIsAString->Attribute("type", "string"))
        {
            std::string value = ThisOneIsAString->GetText();
            std::cout << "Hey.ThisOneIsAString: " << value << std::endl;
        }
    }

    XMLElement* OneMOre = doc.FirstChildElement("OneMOre");
    if (OneMOre)
    {
        XMLElement* mAkEs = OneMOre->FirstChildElement("mAkEs");

        if (mAkEs && mAkEs->Attribute("type", "bool"))
        {
            bool value = std::stoi(mAkEs->GetText());
            std::cout << "OOneMOre.mAkEs: " << value << std::endl;
        }
    }
    
}

int main()
{
    readXml("output.xml");

    return 0;
}