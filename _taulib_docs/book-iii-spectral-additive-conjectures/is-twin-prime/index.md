---
{
  "projection_kind": "taulib_declaration",
  "title": "is_twin_prime",
  "permalink": "/corpus/taulib/docs/book-iii-spectral-additive-conjectures/is-twin-prime/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.AdditiveConjectures`.",
  "declaration_id": "TauLib.BookIII.Spectral.AdditiveConjectures::is_twin_prime",
  "declaration_slug": "is-twin-prime",
  "kind": "def",
  "name": "is_twin_prime",
  "module_name": "TauLib.BookIII.Spectral.AdditiveConjectures",
  "module_url": "/corpus/taulib/docs/book-iii-spectral-additive-conjectures/",
  "source_line_start": 112,
  "source_line_end": 113,
  "registry_ids": [
    "III.D96"
  ],
  "related_registry_items": [
    {
      "id": "III.D96",
      "title": "Twin Prime Distribution",
      "url": "/registry/object/III.D96/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L112-L113",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.AdditiveConjectures",
        "url": "/corpus/taulib/docs/book-iii-spectral-additive-conjectures/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L112-L113",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookIII.Spectral.AdditiveConjectures](/corpus/taulib/docs/book-iii-spectral-additive-conjectures/)
- Source path: [`TauLib/BookIII/Spectral/AdditiveConjectures.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L112-L113)
- Source range: L112-L113
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `III.D96` — Twin Prime Distribution

## Immediate Comment / Docstring

```lean
/-- [III.D96] Is p a twin prime (p and p+2 both prime)? -/
```

## Source Excerpt

```lean
def is_twin_prime (p : Nat) : Bool :=
  is_prime_nat p && is_prime_nat (p + 2)
```
