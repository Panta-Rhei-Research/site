---
{
  "projection_kind": "taulib_declaration",
  "title": "adelic_embedding_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-adeles/adelic-embedding-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.Adeles`.",
  "declaration_id": "TauLib.BookIII.Spectral.Adeles::adelic_embedding_check",
  "declaration_slug": "adelic-embedding-check",
  "kind": "def",
  "name": "adelic_embedding_check",
  "module_name": "TauLib.BookIII.Spectral.Adeles",
  "module_url": "/verify/taulib/docs/book-iii-spectral-adeles/",
  "source_line_start": 110,
  "source_line_end": 130,
  "registry_ids": [
    "III.T12"
  ],
  "related_registry_items": [
    {
      "id": "III.T12",
      "title": "Adelic Embedding Theorem",
      "url": "/registry/object/III.T12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Adeles.lean#L110-L130",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Adeles.lean#L110-L130",
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
- Source path: [`TauLib/BookIII/Spectral/Adeles.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Adeles.lean#L110-L130)
- Source range: L110-L130
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T12` — Adelic Embedding Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T12] Adelic embedding: the map x ↦ (x mod p₁, ..., x mod pₖ)
    is injective on ℤ/Prim(k)ℤ. This is CRT injectivity. -/
```

## Source Excerpt

```lean
def adelic_embedding_check (bound db : TauIdx) : Bool :=
  go 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
where
  go (x y k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if y > bound then go (x + 1) 0 1 (fuel - 1)
    else if k > db then go x (y + 1) 1 (fuel - 1)
    else
      let pk := primorial k
      let xr := if pk > 0 then x % pk else x
      let yr := if pk > 0 then y % pk else y
      -- If adelic images agree, then x ≡ y mod Prim(k)
      let ax := to_adele xr k
      let ay := to_adele yr k
      let images_agree := ax.components == ay.components
      let values_agree := xr == yr
      -- Injectivity: images agree ⟹ values agree
      let ok := if images_agree then values_agree else true
      ok && go x y (k + 1) (fuel - 1)
  termination_by fuel
```
