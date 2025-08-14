import Link from 'next/link';

const Footer = () => {
  return (
    <footer className="bg-gray-800 text-white">
      <div className="container mx-auto py-8 px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {/* About Section */}
          <div>
            <h3 className="text-xl font-bold mb-4">SafeDeny</h3>
            <p className="text-gray-400">
              حلول متكاملة في الأمن السيبراني، الشبكات، والاتصالات الموحدة.
            </p>
          </div>

          {/* Links Section */}
          <div>
            <h3 className="text-lg font-semibold mb-4">روابط سريعة</h3>
            <ul className="space-y-2">
              <li><Link href="/about" className="hover:text-blue-400">عن الشركة</Link></li>
              <li><Link href="/services" className="hover:text-blue-400">خدماتنا</Link></li>
              <li><Link href="/products" className="hover:text-blue-400">منتجاتنا</Link></li>
              <li><Link href="/contact" className="hover:text-blue-400">اتصل بنا</Link></li>
            </ul>
          </div>

          {/* Contact Section */}
          <div>
            <h3 className="text-lg font-semibold mb-4">تواصل معنا</h3>
            <ul className="space-y-2 text-gray-400">
              <li>Email: info@safedeny.com</li>
              <li>Phone: +123 456 7890</li>
              {/* Add social media icons later */}
            </ul>
          </div>
        </div>

        <div className="mt-8 pt-8 border-t border-gray-700 text-center text-gray-500">
          <p>&copy; {new Date().getFullYear()} SafeDeny. جميع الحقوق محفوظة.</p>
          <div className="mt-2">
            <Link href="/privacy-policy" className="hover:text-white mx-2">سياسة الخصوصية</Link>
            |
            <Link href="/terms-of-use" className="hover:text-white mx-2">شروط الاستخدام</Link>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
