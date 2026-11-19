// Generado desde tokens.json por scripts/generate.py. No editar a mano.
package dev.takumi.design

import androidx.compose.foundation.shape.CutCornerShape
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.em
import androidx.compose.ui.unit.sp

/** Las dos familias hay que enlazarlas con los .ttf (OFL) de cada app: res/font/outfit_*.ttf y jetbrains_mono_*.ttf. */
lateinit var TakumiUi: FontFamily
lateinit var TakumiMono: FontFamily

object TakumiColors {
    val Oscuro = darkColorScheme(
        primary = Color(0xFFF2F2F2), onPrimary = Color(0xFF000000),
        secondary = Color(0xFFC9C9C9), onSecondary = Color(0xFF000000),
        tertiary = Color(0xFF8C8C8C), onTertiary = Color(0xFF000000),
        background = Color(0xFF000000), onBackground = Color(0xFFF2F2F2),
        surface = Color(0xFF080808), onSurface = Color(0xFFF2F2F2),
        surfaceVariant = Color(0xFF111111), onSurfaceVariant = Color(0xFF8C8C8C),
        surfaceContainer = Color(0xFF080808), surfaceContainerHigh = Color(0xFF111111),
        outline = Color(0xFF3A3A3A), outlineVariant = Color(0xFF1C1C1C),
        error = Color(0xFFF2F2F2), onError = Color(0xFF000000),
        inverseSurface = Color(0xFFF2F2F2), inverseOnSurface = Color(0xFF000000),
    )

    val Claro = lightColorScheme(
        primary = Color(0xFF0A0A0A), onPrimary = Color(0xFFF4F4F4),
        secondary = Color(0xFF333333), onSecondary = Color(0xFFF4F4F4),
        tertiary = Color(0xFF6B6B6B), onTertiary = Color(0xFFF4F4F4),
        background = Color(0xFFF4F4F4), onBackground = Color(0xFF0A0A0A),
        surface = Color(0xFFFFFFFF), onSurface = Color(0xFF0A0A0A),
        surfaceVariant = Color(0xFFEBEBEB), onSurfaceVariant = Color(0xFF6B6B6B),
        surfaceContainer = Color(0xFFFFFFFF), surfaceContainerHigh = Color(0xFFEBEBEB),
        outline = Color(0xFFC0C0C0), outlineVariant = Color(0xFFE0E0E0),
        error = Color(0xFF0A0A0A), onError = Color(0xFFF4F4F4),
        inverseSurface = Color(0xFF0A0A0A), inverseOnSurface = Color(0xFFF4F4F4),
    )

    /** Escala de grises para gráficos: nunca se usa color para distinguir series. */
    val Grises = listOf(Color(0xFFF2F2F2), Color(0xFFC9C9C9), Color(0xFF8C8C8C), Color(0xFF5E5E5E), Color(0xFF3A3A3A), Color(0xFF1C1C1C))
}

object TakumiShapes {
    /** Corte diagonal del logo en la esquina superior derecha. Radio 0 en el resto. */
    val CorteSm = CutCornerShape(topStart = 0.dp, topEnd = 10.dp, bottomEnd = 0.dp, bottomStart = 0.dp)
    val CorteMd = CutCornerShape(topStart = 0.dp, topEnd = 14.dp, bottomEnd = 0.dp, bottomStart = 0.dp)
    val CorteLg = CutCornerShape(topStart = 0.dp, topEnd = 22.dp, bottomEnd = 0.dp, bottomStart = 0.dp)
    val Recto = CutCornerShape(0.dp)
    val Borde = 1.dp
}

object TakumiType {
        val display = TextStyle(fontFamily = TakumiUi, fontWeight = FontWeight(200), fontSize = 56.sp, letterSpacing = 0.26.em, lineHeight = 84.sp)
        val titulo = TextStyle(fontFamily = TakumiUi, fontWeight = FontWeight(200), fontSize = 32.sp, letterSpacing = 0.02.em, lineHeight = 48.sp)
        val seccion = TextStyle(fontFamily = TakumiUi, fontWeight = FontWeight(500), fontSize = 14.sp, letterSpacing = 0.22.em, lineHeight = 21.sp)
        val cuerpo = TextStyle(fontFamily = TakumiUi, fontWeight = FontWeight(300), fontSize = 16.sp, letterSpacing = 0.0.em, lineHeight = 24.sp)
        val pequeno = TextStyle(fontFamily = TakumiUi, fontWeight = FontWeight(300), fontSize = 13.sp, letterSpacing = 0.0.em, lineHeight = 20.sp)
        val etiqueta = TextStyle(fontFamily = TakumiMono, fontWeight = FontWeight(400), fontSize = 12.sp, letterSpacing = 0.2.em, lineHeight = 18.sp)
        val dato = TextStyle(fontFamily = TakumiMono, fontWeight = FontWeight(400), fontSize = 14.sp, letterSpacing = 0.0.em, lineHeight = 21.sp)
}

object TakumiMotion {
    const val Rapido = 120; const val Normal = 200; const val Lento = 300; const val Revelado = 800
    val Curva = androidx.compose.animation.core.CubicBezierEasing(0.2f, 0.7f, 0.2f, 1.0f)
}
