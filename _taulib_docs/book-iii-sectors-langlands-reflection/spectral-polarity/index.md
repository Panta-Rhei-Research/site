---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_polarity",
  "permalink": "/verify/taulib/docs/book-iii-sectors-langlands-reflection/spectral-polarity/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Sectors.LanglandsReflection`.",
  "declaration_id": "TauLib.BookIII.Sectors.LanglandsReflection::spectral_polarity",
  "declaration_slug": "spectral-polarity",
  "kind": "def",
  "name": "spectral_polarity",
  "module_name": "TauLib.BookIII.Sectors.LanglandsReflection",
  "module_url": "/verify/taulib/docs/book-iii-sectors-langlands-reflection/",
  "source_line_start": 148,
  "source_line_end": 161,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L148-L161",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L148-L161",
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
- Source path: [`TauLib/BookIII/Sectors/LanglandsReflection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L148-L161)
- Source range: L148-L161
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D17` — Spectral Polarity

## Immediate Comment / Docstring

```lean
/-- [III.D17] Spectral polarity of a sector at finite cutoff.
    Measures the m-axis (Galois/B-lobe) vs n-axis (automorphic/C-lobe)
    balance DIRECTLY from the character lattice.
    Returns (m_sum, n_sum) over characters in the sector. -/
```

## Source Excerpt

```lean
def spectral_polarity (sec : Sector) (bound : TauIdx) : (TauIdx × TauIdx) :=
  go 0 0 0 0 ((bound + 1) * (bound + 1))
where
  go (m n m_acc n_acc fuel : Nat) : (TauIdx × TauIdx) :=
    if fuel = 0 then (m_acc, n_acc)
    else if m > bound then (m_acc, n_acc)
    else if n > bound then go (m + 1) 0 m_acc n_acc (fuel - 1)
    else
      let χ : BoundaryCharacter := ⟨Int.ofNat m, Int.ofNat n⟩
      let (m_acc', n_acc') := if sector_of χ == sec then
        (m_acc + m, n_acc + n)
      else (m_acc, n_acc)
      go m (n + 1) m_acc' n_acc' (fuel - 1)
  termination_by fuel
```
