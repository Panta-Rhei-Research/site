---
{
  "projection_kind": "taulib_declaration",
  "title": "twin_primes_30",
  "permalink": "/corpus/taulib/docs/book-iii-spectral-additive-conjectures/twin-primes-30/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.AdditiveConjectures`.",
  "declaration_id": "TauLib.BookIII.Spectral.AdditiveConjectures::twin_primes_30",
  "declaration_slug": "twin-primes-30",
  "kind": "theorem",
  "name": "twin_primes_30",
  "module_name": "TauLib.BookIII.Spectral.AdditiveConjectures",
  "module_url": "/corpus/taulib/docs/book-iii-spectral-additive-conjectures/",
  "source_line_start": 199,
  "source_line_end": 200,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L199-L200",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L199-L200",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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
- Source path: [`TauLib/BookIII/Spectral/AdditiveConjectures.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L199-L200)
- Source range: L199-L200
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.D96` — Twin Prime Distribution

## Immediate Comment / Docstring

```lean
/-- [III.D96] At least 5 twin prime pairs below 30: (3,5),(5,7),(11,13),(17,19),(29,31). -/
```

## Source Excerpt

```lean
theorem twin_primes_30 :
    twin_prime_count 30 >= 5 := by native_decide
```
