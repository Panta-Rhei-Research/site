---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_polarity_check",
  "permalink": "/verify/taulib/docs/book-iii-sectors-langlands-reflection/spectral-polarity-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Sectors.LanglandsReflection`.",
  "declaration_id": "TauLib.BookIII.Sectors.LanglandsReflection::spectral_polarity_check",
  "declaration_slug": "spectral-polarity-check",
  "kind": "def",
  "name": "spectral_polarity_check",
  "module_name": "TauLib.BookIII.Sectors.LanglandsReflection",
  "module_url": "/verify/taulib/docs/book-iii-sectors-langlands-reflection/",
  "source_line_start": 168,
  "source_line_end": 181,
  "registry_ids": [
    "III.D17"
  ],
  "related_registry_items": [
    {
      "id": "III.D17",
      "title": "Spectral Polarity",
      "url": "/registry/object/III.D17/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L168-L181",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L168-L181",
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
- Source path: [`TauLib/BookIII/Sectors/LanglandsReflection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L168-L181)
- Source range: L168-L181
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D17` — Spectral Polarity

## Immediate Comment / Docstring

```lean
/-- [III.D17] Check spectral polarity classification:
    - D: both zero (trivial character only)
    - A: BALANCED (m_sum = n_sum)
    - B: m-dominant (m_sum > n_sum)
    - C: n-dominant (n_sum > m_sum) -/
```

## Source Excerpt

```lean
def spectral_polarity_check (bound : TauIdx) : Bool :=
  let (d_m, d_n) := spectral_polarity .D bound
  let (a_m, a_n) := spectral_polarity .A bound
  let (b_m, b_n) := spectral_polarity .B bound
  let (c_m, c_n) := spectral_polarity .C bound
  -- D: both zero (only (0,0) is in D-sector)
  let d_ok := d_m == 0 && d_n == 0
  -- A: balanced (characters have |m| = |n|, so m_sum = n_sum)
  let a_ok := a_m == a_n
  -- B: m-dominant (characters have |m| > |n| and n = 0, so m_sum > 0, n_sum = 0)
  let b_ok := b_m > b_n
  -- C: n-dominant (characters have |n| > |m| and m = 0, so n_sum > 0, m_sum = 0)
  let c_ok := c_m < c_n
  d_ok && a_ok && b_ok && c_ok
```
