---
{
  "projection_kind": "taulib_declaration",
  "title": "adele_mul",
  "permalink": "/verify/taulib/docs/book-iii-spectral-adeles/adele-mul/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.Adeles`.",
  "declaration_id": "TauLib.BookIII.Spectral.Adeles::adele_mul",
  "declaration_slug": "adele-mul",
  "kind": "def",
  "name": "adele_mul",
  "module_name": "TauLib.BookIII.Spectral.Adeles",
  "module_url": "/verify/taulib/docs/book-iii-spectral-adeles/",
  "source_line_start": 64,
  "source_line_end": 76,
  "registry_ids": [
    "III.D22"
  ],
  "related_registry_items": [
    {
      "id": "III.D22",
      "title": "τ-Adele Ring",
      "url": "/registry/object/III.D22/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Adeles.lean#L64-L76",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.Adeles",
        "url": "/verify/taulib/docs/book-iii-spectral-adeles/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Adeles.lean#L64-L76",
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

- Module: [TauLib.BookIII.Spectral.Adeles](/verify/taulib/docs/book-iii-spectral-adeles/)
- Source path: [`TauLib/BookIII/Spectral/Adeles.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Adeles.lean#L64-L76)
- Source range: L64-L76
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D22` — τ-Adele Ring

## Immediate Comment / Docstring

```lean
/-- [III.D22] Adele multiplication: component-wise multiplication mod p_i. -/
```

## Source Excerpt

```lean
def adele_mul (a b : AdeleElement) : AdeleElement :=
  let k := a.depth
  let comps := go a.components b.components 0 k []
  ⟨k, comps⟩
where
  go (as_ bs : List TauIdx) (i k : Nat) (acc : List TauIdx) : List TauIdx :=
    if i >= k then acc
    else
      let p := nth_prime (i + 1)
      let ai := as_.getD i 0
      let bi := bs.getD i 0
      let ci := if p > 0 then (ai * bi) % p else 0
      go as_ bs (i + 1) k (acc ++ [ci])
```
