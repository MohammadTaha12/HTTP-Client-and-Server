import Link from 'next/link';

const Header = () => {
  return (
    <header className="bg-white shadow-md">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <div className="flex-shrink-0">
            <Link href="/" className="text-2xl font-bold text-gray-800">
              SafeDeny
            </Link>
          </div>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex md:space-x-8">
            <Link href="/" className="text-gray-600 hover:text-blue-600">
              الرئيسية
            </Link>
            <Link href="/about" className="text-gray-600 hover:text-blue-600">
              عن الشركة
            </Link>
            <Link href="/products" className="text-gray-600 hover:text-blue-600">
              المنتجات
            </Link>
            <Link href="/services" className="text-gray-600 hover:text-blue-600">
              الخدمات
            </Link>
            <Link href="/blog" className="text-gray-600 hover:text-blue-600">
              المدونة
            </Link>
            <Link href="/contact" className="text-gray-600 hover:text-blue-600">
              اتصل بنا
            </Link>
          </nav>

          {/* Mobile Menu Button */}
          <div className="md:hidden flex items-center">
            <button className="outline-none mobile-menu-button">
              <svg
                className="w-6 h-6 text-gray-600 hover:text-blue-600"
                fill="none"
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path d="M4 6h16M4 12h16m-7 6h7"></path>
              </svg>
            </button>
          </div>
        </div>
      </div>
      {/* Mobile Menu (hidden by default) will be implemented later */}
    </header>
  );
};

export default Header;
