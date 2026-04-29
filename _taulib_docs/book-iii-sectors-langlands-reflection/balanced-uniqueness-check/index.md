---
{
  "projection_kind": "taulib_declaration",
  "title": "balanced_uniqueness_check",
  "permalink": "/verify/taulib/docs/book-iii-sectors-langlands-reflection/balanced-uniqueness-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Sectors.LanglandsReflection`.",
  "declaration_id": "TauLib.BookIII.Sectors.LanglandsReflection::balanced_uniqueness_check",
  "declaration_slug": "balanced-uniqueness-check",
  "kind": "def",
  "name": "balanced_uniqueness_check",
  "module_name": "TauLib.BookIII.Sectors.LanglandsReflection",
  "module_url": "/verify/taulib/docs/book-iii-sectors-langlands-reflection/",
  "source_line_start": 189,
  "source_line_end": 199,
  "registry_ids": [
    "III.P04"
  ],
  "related_registry_items": [
    {
      "id": "III.P04",
      "title": "Balanced Sector Uniqueness",
      "url": "/registry/object/III.P04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L189-L199",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Sectors.LanglandsReflection",
        "url": "/verify/taulib/docs/book-iii-sectors-langlands-reflection/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L189-L199",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookIII.Sectors.LanglandsReflection](/verify/taulib/docs/book-iii-sectors-langlands-reflection/)
- Source path: [`TauLib/BookIII/Sectors/LanglandsReflection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L189-L199)
- Source range: L189-L199
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P04` — Balanced Sector Uniqueness

## Immediate Comment / Docstring

```lean
/-- [III.P04] Balanced sector uniqueness: among primitive sectors {D, A, B, C},
    only the A-sector has balanced spectral polarity (m_sum = n_sum > 0). -/
```

## Source Excerpt

```lean
def balanced_uniqueness_check (bound : TauIdx) : Bool :=
  let (a_m, a_n) := spectral_polarity .A bound
  let (b_m, b_n) := spectral_polarity .B bound
  let (c_m, c_n) := spectral_polarity .C bound
  -- A is balanced and non-trivial
  let a_balanced := a_m == a_n && a_m > 0
  -- B is NOT balanced
  let b_not_balanced := b_m != b_n
  -- C is NOT balanced
  let c_not_balanced := c_m != c_n
  a_balanced && b_not_balanced && c_not_balanced
```
