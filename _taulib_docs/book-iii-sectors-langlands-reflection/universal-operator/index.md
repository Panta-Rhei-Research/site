---
{
  "projection_kind": "taulib_declaration",
  "title": "universal_operator",
  "permalink": "/verify/taulib/docs/book-iii-sectors-langlands-reflection/universal-operator/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Sectors.LanglandsReflection`.",
  "declaration_id": "TauLib.BookIII.Sectors.LanglandsReflection::universal_operator",
  "declaration_slug": "universal-operator",
  "kind": "def",
  "name": "universal_operator",
  "module_name": "TauLib.BookIII.Sectors.LanglandsReflection",
  "module_url": "/verify/taulib/docs/book-iii-sectors-langlands-reflection/",
  "source_line_start": 109,
  "source_line_end": 119,
  "registry_ids": [
    "III.D16"
  ],
  "related_registry_items": [
    {
      "id": "III.D16",
      "title": "Universal Operator",
      "url": "/registry/object/III.D16/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L109-L119",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L109-L119",
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
- Source path: [`TauLib/BookIII/Sectors/LanglandsReflection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L109-L119)
- Source range: L109-L119
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D16` — Universal Operator

## Immediate Comment / Docstring

```lean
/-- [III.D16] Universal operator H_{≤N} on characters at finite cutoff.
    At stage k: H_{≤N}(χ)(x) = Σ_{j ≤ N} weight(χ) · reduce(j, k).
    This is the finite-cutoff truncation of the universal spectral operator.
    All L-functions are spectral determinants of this operator. -/
```

## Source Excerpt

```lean
def universal_operator (χ : BoundaryCharacter) (_x k bound : TauIdx) : TauIdx :=
  let weight := χ.m_index.natAbs + χ.n_index.natAbs
  go weight 0 0 (bound + 1)
where
  go (w j acc fuel : Nat) : TauIdx :=
    if fuel = 0 then reduce acc k
    else if j > bound then reduce acc k
    else
      let contrib := w * reduce j k
      go w (j + 1) (acc + contrib) (fuel - 1)
  termination_by fuel
```
