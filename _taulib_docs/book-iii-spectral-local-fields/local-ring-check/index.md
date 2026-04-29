---
{
  "projection_kind": "taulib_declaration",
  "title": "local_ring_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-local-fields/local-ring-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.LocalFields`.",
  "declaration_id": "TauLib.BookIII.Spectral.LocalFields::local_ring_check",
  "declaration_slug": "local-ring-check",
  "kind": "def",
  "name": "local_ring_check",
  "module_name": "TauLib.BookIII.Spectral.LocalFields",
  "module_url": "/verify/taulib/docs/book-iii-spectral-local-fields/",
  "source_line_start": 84,
  "source_line_end": 105,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/LocalFields.lean#L84-L105",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/LocalFields.lean#L84-L105",
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
- Source path: [`TauLib/BookIII/Spectral/LocalFields.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/LocalFields.lean#L84-L105)
- Source range: L84-L105
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D21` — τ-Native Local Field

## Immediate Comment / Docstring

```lean
/-- [III.D21] Local field ring operations: addition and multiplication
    are well-defined on ℤ/p^dℤ. -/
```

## Source Excerpt

```lean
def local_ring_check (bound depth : TauIdx) : Bool :=
  go 0 0 1 ((bound + 1) * (bound + 1) * (depth + 1))
where
  go (x y d fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if y > bound then go (x + 1) 0 1 (fuel - 1)
    else if d > depth then go x (y + 1) 1 (fuel - 1)
    else
      -- Use p = 3 as test prime (nth_prime 2)
      let p : Nat := 3
      let pd := p ^ d
      if pd == 0 then go x y (d + 1) (fuel - 1)
      else
        let xm := x % pd
        let ym := y % pd
        -- Addition: (x+y) mod p^d = ((x mod p^d) + (y mod p^d)) mod p^d
        let add_ok := (x + y) % pd == (xm + ym) % pd
        -- Multiplication: similar
        let mul_ok := (x * y) % pd == (xm * ym) % pd
        add_ok && mul_ok && go x y (d + 1) (fuel - 1)
  termination_by fuel
```
