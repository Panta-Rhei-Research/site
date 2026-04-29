---
{
  "projection_kind": "taulib_declaration",
  "title": "local_field_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-local-fields/local-field-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.LocalFields`.",
  "declaration_id": "TauLib.BookIII.Spectral.LocalFields::local_field_check",
  "declaration_slug": "local-field-check",
  "kind": "def",
  "name": "local_field_check",
  "module_name": "TauLib.BookIII.Spectral.LocalFields",
  "module_url": "/verify/taulib/docs/book-iii-spectral-local-fields/",
  "source_line_start": 61,
  "source_line_end": 80,
  "registry_ids": [
    "III.D21"
  ],
  "related_registry_items": [
    {
      "id": "III.D21",
      "title": "τ-Native Local Field",
      "url": "/registry/object/III.D21/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/LocalFields.lean#L61-L80",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.LocalFields",
        "url": "/verify/taulib/docs/book-iii-spectral-local-fields/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/LocalFields.lean#L61-L80",
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

- Module: [TauLib.BookIII.Spectral.LocalFields](/verify/taulib/docs/book-iii-spectral-local-fields/)
- Source path: [`TauLib/BookIII/Spectral/LocalFields.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/LocalFields.lean#L61-L80)
- Source range: L61-L80
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D21` — τ-Native Local Field

## Immediate Comment / Docstring

```lean
/-- [III.D21] Local field check: verify inverse system property.
    For each p and depth d: reduce from p^(d+1) to p^d is coherent. -/
```

## Source Excerpt

```lean
def local_field_check (bound depth : TauIdx) : Bool :=
  go 0 1 1 ((bound + 1) * (depth + 1) * 5)
where
  go (x p_idx d fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if p_idx > 4 then go (x + 1) 1 1 (fuel - 1)
    else if d >= depth then go x (p_idx + 1) 1 (fuel - 1)
    else
      let p := nth_prime p_idx
      if p < 2 then go x (p_idx + 1) 1 (fuel - 1)
      else
        let pd := p ^ d
        let pd1 := p ^ (d + 1)
        -- Inverse system: (x mod p^(d+1)) mod p^d = x mod p^d
        let high := if pd1 > 0 then x % pd1 else 0
        let projected := if pd > 0 then high % pd else 0
        let low := if pd > 0 then x % pd else 0
        projected == low && go x p_idx (d + 1) (fuel - 1)
  termination_by fuel
```
