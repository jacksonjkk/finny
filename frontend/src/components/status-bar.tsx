import { MdOutlineContactSupport } from "react-icons/md";

export const StatusBar = () => {
  return (
    <div className="py-5 fixed bottom-0 w-screen left-0 bg-background z-50">
      <div className="w-7xl flex items-center justify-between mx-auto">
        <div className="flex items-center space-x-4 w-fit">
          <span className="text-sm font-medium">Copyright &copy; 2026</span>
        </div>
        <div className="flex items-center space-x-4 w-fit">
          <span className="text-sm font-medium">Help</span>
          <MdOutlineContactSupport />
        </div>
      </div>
    </div>
  );
};
